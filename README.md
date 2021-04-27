# Selenium Headless

This project helps me to run some Selenium tests written in Python into a Docker container, and during Gitlab pipeline execution.

You can have a look on the base Dockerfile and find more explanation on the [GitHub of the project](https://github.com/drkms/selenium-headless)

This image may help you to run tests inside a container from command line on the host system.

Supposing you have a test, or many of them, with the name obviously ending with ".py" extension, you can run :
```shell
docker run -v$PWD:/test -ti selenium-headless:3.0 python -m pytest *.py
```

The build of the selenium-headless:3.0 works with Firefox 88 and Geckodriver 0.29.1.

Note that for the install, the last line of the Dockerfile (default behaviour) doesnt work as expected. I stil have to fix it ^^'g

