

import os

class Config(object):
    # get a token from @BotFather
    USER_SESSION = os.environ.get("USER_SESSION", "BAFCkV0AI2lCxFxXOqoRJo0hYAjqQmpvaP_7vdn3zu--s965kphPj65XxTuHKw_hFhDz5RC6Wl_rmenodHzOhSeMNogBNVcHvD_cF2pgSJKRaW65G539OFnVvyQuuds_PEk4hZfptI2VH0Y5i_yPrMUby_3Xo78e5EosLj9ad6gEuf0dVtS1ju9DkujQfyt8vnw76oT0nLDKyn95YMeWojE340eMeENeKapHaAesV0N5hrRa3HC74gzcEST-e3bQa99YyIhz2pYIZ9u7D5udrvUlMCyAPQsjasUPLTrgtb2iAkHEvOhNuHO2sv4JzI8KDutScXCTeTSa_-UC7XPBnUHCgB4dagAAAAGQjzJvAA")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "21139805"))
    API_HASH = os.environ.get("API_HASH", "1b67868ac541b3599100ba969b3de474")
    AUTH_USERS = os.environ.get("OWNER", "6720270959")


