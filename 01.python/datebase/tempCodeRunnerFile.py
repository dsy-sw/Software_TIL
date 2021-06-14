from app_base import Application


class AddrBookApp(Application):
    def __init__(self):
        super().__init__()
        print(self.config)


if __name__ == "__main__":
    app = AddrBookApp()
