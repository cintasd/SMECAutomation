class BasePage:
    def __init__(self, page, base_url: str = "https://devhub.mysmec.com"):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = "/"):
        self.page.goto(f"{self.base_url}{path}", wait_until="domcontentloaded", timeout=30000)

    def get_title(self) -> str:
        return self.page.title()

    def assert_url_contains(self, fragment: str):
        assert fragment.lower() in self.page.url.lower(), f"Expected URL to contain '{fragment}', got {self.page.url}"
