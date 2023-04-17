CURRENT=$(pwd)
cd ../..
python setup.py build_ext --inplace
cd $CURRENT