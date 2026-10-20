from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.hero_heading = page.locator('h1').first
        self.course_link = lambda course_name: page.locator(f'a[href="/{course_name.lower()}"]').first

    def open_homepage(self):
        self.page.goto("https://devhub.mysmec.com/", wait_until="domcontentloaded", timeout=30000)
        self.page.bring_to_front()
        return self

    def get_heading(self) -> str:
        return self.hero_heading.inner_text().strip()

    def click_course(self, course_name):
        self.course_link(course_name).click()
        self.page.wait_for_url(f"**/{course_name.lower()}")
        return self
