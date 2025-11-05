class Person:
    def __init__(self, name, privacy, biography):
        self.name = name
        self.privacy = privacy  # 'P' = Public, 'U' = Private
        self.biography = biography

    def get_name(self):
        return self.name

    def get_privacy(self):
        return self.privacy

    def get_biography(self):
        return self.biography
