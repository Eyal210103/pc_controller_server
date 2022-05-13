import logging
import winapps


class SoftwareListDispatcher:
    @staticmethod
    def dispatch():
        apps = [app.name for app in winapps.list_installed()]
        logging.info("SoftwareListDispatcher", "found:", apps)
        return apps
