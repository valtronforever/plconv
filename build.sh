#!/bin/bash

PACKAGE_NAME="plconv"
VERSION="1.1-1"
BASEDIR=$(dirname "$0")/build

for DISTRO in bionic focal
do


FULLNAME="${PACKAGE_NAME}_${VERSION}${DISTRO}"
DIST_DIR=${BASEDIR}/${DISTRO}/dist

sudo rm -rf ${DIST_DIR}
mkdir -p ${DIST_DIR}/${FULLNAME}/opt/pharmstudio
mkdir -p ${DIST_DIR}/${FULLNAME}/usr/bin
mkdir -p ${DIST_DIR}/${FULLNAME}/DEBIAN
mkdir -p ${DIST_DIR}/${FULLNAME}/usr/share/icons/hicolor/scalable/apps
mkdir -p ${DIST_DIR}/${FULLNAME}/usr/share/applications

sudo docker build -f ${BASEDIR}/Dockerfile-${DISTRO} . -t ${DISTRO}-build
sudo docker create -ti --name dummy ${DISTRO}-build bash
sudo docker cp dummy:/opt/pharmstudio/plconv ${DIST_DIR}/${FULLNAME}/opt/pharmstudio
sudo docker rm -f dummy
sudo chown -R user.user ${DIST_DIR}
cp $(dirname "$0")/data/plconv.svg ${DIST_DIR}/${FULLNAME}/usr/share/icons/hicolor/scalable/apps/
cp $(dirname "$0")/data/plconv.desktop ${DIST_DIR}/${FULLNAME}/usr/share/applications


/bin/cat <<EOF > ${DIST_DIR}/${FULLNAME}/usr/bin/${PACKAGE_NAME}
#!/bin/sh
cd /opt/pharmstudio/plconv
/opt/pharmstudio/plconv/.env/bin/python /opt/pharmstudio/plconv/run.py
exit 0
EOF
chmod +x ${DIST_DIR}/${FULLNAME}/usr/bin/${PACKAGE_NAME}

/bin/cat <<EOF > ${DIST_DIR}/${FULLNAME}/DEBIAN/control
Package: ${PACKAGE_NAME}
Version: ${VERSION}${DISTRO}
Section: base
Priority: optional
Architecture: amd64
Maintainer: Valentin Osipenko <valtron.forever@gmail.com>
Depends: python3-gi-cairo, gobject-introspection, gir1.2-gtk-3.0
Description: Pharmstudio plconv
 Pricelist converter for pharmstudio
EOF

/bin/cat <<EOF > ${DIST_DIR}/${FULLNAME}/DEBIAN/prerm
#!/bin/sh
py3clean /opt/pharmstudio/plconv
exit 0
EOF
chmod +x ${DIST_DIR}/${FULLNAME}/DEBIAN/prerm

cd $DIST_DIR
dpkg-deb --build $FULLNAME
cd ../../..

done
