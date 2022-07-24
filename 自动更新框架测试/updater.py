import sys
import os

APPCAST_URL = 'https://ydjisi.com/test/SampleAppcast.xml'
SPARKLE_PATH = '/Users/chensuilong/Downloads/Sparkle-1.13.1/Sparkle.framework'

def get_updater():
    print("sys.platform",sys.platform)
    if sys.platform == 'darwin' and getattr(sys, 'frozen', False) is False:
        """
        Use Sparkle framework on macOS.
        Settings: https://sparkle-project.org/documentation/customization/
        Examples: https://programtalk.com/python-examples/objc.loadBundle/
        To debug:
        $ defaults read com.borgbase.client.macos
        """

        import objc
        import Cocoa
        # bundle_path = os.path.join(os.path.dirname(sys.executable), os.pardir, 'Frameworks', 'Sparkle.framework')
        bundle_path = SPARKLE_PATH
        objc.loadBundle('Sparkle', globals(), bundle_path)
        sparkle = SUUpdater.sharedUpdater()  # noqa: F821

        # A default Appcast URL is set in vorta.spec, when setting it here it's saved to defaults,
        # so we need both cases.
        # appcast_nsurl = Cocoa.NSURL.URLWithString_('https://borgbase.github.io/vorta/appcast-pre.xml')
        appcast_nsurl = Cocoa.NSURL.URLWithString_(APPCAST_URL)

        sparkle.setFeedURL_(appcast_nsurl)

        sparkle.setAutomaticallyChecksForUpdates_(True)
        sparkle.checkForUpdatesInBackground()

        return sparkle

    else:  # TODO: implement for Linux
        return None