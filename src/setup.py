from setuptools import setup
import setup_translate

pkg = 'Extensions.ZapStatistic'
setup(name='enigma2-plugin-extensions-zapstatistic',
       version='3.0',
       description='Shows the watched services with some statistic',
       package_dir={pkg: 'ZapStatistic'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
