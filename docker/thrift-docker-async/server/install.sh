sudo apt-get install libboost-dev libboost-test-dev libboost-program-options-dev libboost-filesystem-dev libboost-thread-dev libevent-dev automake libtool flex bison pkg-config g++ libssl-dev;
wget https://dlcdn.apache.org/thrift/0.17.0/thrift-0.17.0.tar.gz;
tar -xvzf thrift-0.17.0.tar.gz;
cd thrift-0.17.0;
./bootstrap.sh;
./configure --with-python --without-php --without-netstd;
make;
make install;
thrift;
sudo make install;