FILES :=							\
	.gitignore						\
    .travis.yml						\
    apiary.apib						\
    IDB1.log						\
    models.html						\
    models.py						\
    tests.py						\
    server.py						\
    UML.pdf							

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__
	rm -f tests.tmp

config:
	git config -l

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: tests.out

models.html: models.py
	pydoc -w models

IDB1.log:
	git log > IDB1.log

tests.out: tests.py
	coverage run tests.py
	coverage report --include=models.py
