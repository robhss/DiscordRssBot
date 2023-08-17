from configparser import ConfigParser

class ConfigManager:

    def __init__(self, file):
        self.file = file
        self.config = ConfigParser()
        self.config.read(file)

    def get_objectindex(self,section: str, object: str) -> str:
        for i in self.config.items(section):
            if i[1] == object:
                return i[0]

    def get_objects_from_section(self,section: str) -> list[str]:
        result = []

        if self.config.has_section(section):
            for item in self.config[section]:
                result.append(self.config[section][item])

        return result

    def add_object_to_section(self,section: str, url: str):
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(section,section + '_' + str(len(self.config.options(section)) + 1) ,url)

        with open(self.file, 'w') as f:
            self.config.write(f)

        self.update()

    def remove_object_from_section(self, section: str, url: str):

        for item in self.config[section]:
            if self.config[section][item] == url:
                self.config.remove_option(section, item)

        with open(self.file, 'w') as f:
            self.config.write(f)

        self.update()

    def update(self):
        self.config.read(self.file)



