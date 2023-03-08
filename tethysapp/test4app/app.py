from tethys_sdk.base import TethysAppBase


class Test4App(TethysAppBase):
    """
    Tethys app class for Test4App.
    """

    name = 'Test4App'
    description = ''
    package = 'test4app'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test4app'
    color = '#718093'
    tags = ''
    enable_feedback = False
    feedback_emails = []