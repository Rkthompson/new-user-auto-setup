class NewUserRequest():
    """The selection of values submitted by management to create a new user."""

    """constructor"""
    def __init__(self, name, job_title, division, department,
                 model_account_after, need_adobe_cc, need_exacqvision,
                 need_ftp, need_promail) -> None:
        self.name = name
        self.job_title = job_title
        self.division = division
        self.department = department
        self.model_account_after = model_account_after
        self.need_adobe_cc = need_adobe_cc
        self.need_exacqvision = need_exacqvision
        self.need_ftp = need_ftp
        self.need_promail = need_promail

    """Common python practice is to avoid creating setters and getters unless
    they offer additional functionality beyond a traditional setter or
    getter.

    If needed, create using Python property decorators.  Example of class with
    setter and getter in Python:

        class Foo(object):

        def __init__(self):
            self._something = 0

        @property
        def something(self):
            # other stuff happening here
            return self._something

        @something.setter
        def something(self, value):
            # other stuff happening here
            self._something = value

    """

    """setters"""

    """getters"""

    """other functions"""
