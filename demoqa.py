import time

from base import Base

class Demoqa(Base):

    def get_elements_page(self, xpath):
        self.click_on_element(xpath)

    def get_check_box_page(self, xpath):
        self.click_on_element(xpath)

    def select_word_file(self):
        home_directory = self.click_on_element('//*[@id="tree-node"]/ol/li/span/button')
        downloads_directory = self.click_on_element('//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
        word_file = self.click_on_element('//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[3]')
        element = self.get_element('//*[@id="result"]/span[2]').text
        return element





