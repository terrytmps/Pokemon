class StatusStrategy:

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_status_message(self):
        return self.status.get_status_message()

    def get_status_code(self):
        return self.status.get_status_code()

    def get_status_type(self):
        return self.status.get_status_type()