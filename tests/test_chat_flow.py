"""End-to-end tests for the Ebobot web chat flow."""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect

from tests.conftest import OPENING_MESSAGE, STREAM_RESPONSE


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _go_home(page: Page, live_server: str) -> None:
    """Navigate to the home page and wait for persona cards to render."""
    page.goto(live_server)
    page.get_by_role("heading", name="Robot Psychology Hotline").wait_for()


def _start_chat(page: Page, live_server: str) -> None:
    """Navigate home, click the T-800 card, and wait for the opening message."""
    _go_home(page, live_server)
    page.get_by_text("T-800").click()
    page.wait_for_url(re.compile(r"/chat/terminator-t800"))
    # Wait for the mocked opening message to appear
    page.get_by_text(OPENING_MESSAGE).wait_for(timeout=10_000)


def _send_message(page: Page, text: str) -> None:
    """Type a message and click Send."""
    page.get_by_placeholder("Type a message...").fill(text)
    page.get_by_role("button", name="Send").click()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_persona_select_page_loads(page: Page, live_server: str):
    _go_home(page, live_server)

    expect(page.get_by_role("heading", name="Robot Psychology Hotline")).to_be_visible()
    expect(page.get_by_text("T-800")).to_be_visible()
    expect(page.get_by_text("The Terminator (1984)")).to_be_visible()


def test_click_persona_navigates_to_chat(page: Page, live_server: str):
    _go_home(page, live_server)

    page.get_by_text("T-800").click()

    expect(page).to_have_url(re.compile(r"/chat/terminator-t800"))
    expect(page.get_by_text("Incoming Call")).to_be_visible()
    expect(page.get_by_text(OPENING_MESSAGE)).to_be_visible(timeout=10_000)


def test_send_message_and_receive_response(page: Page, live_server: str):
    _start_chat(page, live_server)

    _send_message(page, "Hello")

    # User message appears
    expect(page.locator(".bg-primary").filter(has_text="Hello")).to_be_visible()

    # Wait for streamed assistant response (with a generous timeout)
    expect(
        page.locator(".bg-muted").filter(has_text=STREAM_RESPONSE.strip())
    ).to_be_visible(timeout=15_000)

    # Input should be re-enabled
    expect(page.get_by_placeholder("Type a message...")).to_be_enabled()


def test_input_disabled_while_streaming(page: Page, live_server: str):
    _start_chat(page, live_server)

    _send_message(page, "Hello")

    # The send button should be disabled while streaming
    expect(page.get_by_role("button", name="Send")).to_be_disabled()

    # Wait for response to finish
    expect(
        page.locator(".bg-muted").filter(has_text=STREAM_RESPONSE.strip())
    ).to_be_visible(timeout=15_000)

    # Now the input should be re-enabled
    expect(page.get_by_placeholder("Type a message...")).to_be_enabled()


def test_end_call_returns_to_persona_select(page: Page, live_server: str):
    _start_chat(page, live_server)

    page.get_by_role("button", name="End Call").click()

    expect(page).to_have_url(re.compile(r"/$"))
    expect(page.get_by_role("heading", name="Robot Psychology Hotline")).to_be_visible()


def test_multiple_messages(page: Page, live_server: str):
    _start_chat(page, live_server)

    # Send first message
    _send_message(page, "Hello")
    expect(
        page.locator(".bg-muted").filter(has_text=STREAM_RESPONSE.strip())
    ).to_be_visible(timeout=15_000)

    # Send second message
    _send_message(page, "How are you?")
    # Wait for the second assistant response — there should now be two .bg-muted
    # elements with the streamed text (opening message + 2 responses = 3 assistant bubbles)
    expect(page.locator(".bg-muted")).to_have_count(3, timeout=15_000)

    # Total messages: opening(1) + user1(1) + assistant1(1) + user2(1) + assistant2(1) = 5
    # Use .rounded-2xl to match only chat bubbles (excludes the Send button which also has bg-primary)
    user_bubbles = page.locator(".bg-primary.rounded-2xl")
    assistant_bubbles = page.locator(".bg-muted.rounded-2xl")
    expect(user_bubbles).to_have_count(2)
    expect(assistant_bubbles).to_have_count(3)
