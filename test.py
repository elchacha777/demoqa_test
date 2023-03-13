from demoqa import Demoqa

def test_demoqa():
    d = Demoqa('https://demoqa.com/')
    d.get_page()
    d.get_elements_page('//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5')
    d.get_check_box_page('//*[@id="item-1"]/span')
    element = d.select_word_file()
    d.close_context()
    assert 'wordFile' in element


if __name__ == '__main__':
    test_demoqa()