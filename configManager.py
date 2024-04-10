from configparser import ConfigParser


class ConfigManager:

    def __init__(self, file):
        self.file = file
        self.config = ConfigParser()
        self.config.read(file)

    def is_url_in_section(self, section: str, url: str) -> bool:
        if not self.config.has_section(section):
            return False
        if url in self.config[section].values():
            return True
        return False

    def get_urls_from_section(self, section: str) -> dict[str, str]:

        return dict(self.config[section])

    def add_url_to_section(self, section: str, url: str):
        if not self.config.has_section(section):
            self.config.add_section(section)
            self.config.set(section, f'{section[:len(section)-1]}_1', url)
        else:
            last = self.config.options(section)[-1]

            self.config.set(section, f'{section[:len(section)-1]}_{str(int(last[last.rfind("_") + 1:]) + 1)}', url)

        with open(self.file, 'w') as f:
            self.config.write(f)

        self.update()

    def remove_url_from_section(self, section: str, key: str):

        self.config.remove_option(section, key)

        with open(self.file, 'w') as f:
            self.config.write(f)

        self.update()

    def update(self):
        self.config.read(self.file)
