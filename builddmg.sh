#!/bin/sh
# 创建dmg目录
mkdir -p dist/dmg
# 删除dmg文件夹的文件
rm -r dist/dmg/*
# 复制编译好的app
cp -r "dist/QtEsayDesigner.app" dist/dmg
# 如果dmg文件存在就删除
test -f "dist/QtEsayDesigner.dmg" && rm "dist/QtEsayDesigner.dmg"
create-dmg \
  --volname "QtEsayDesigner" \
  --volicon "QtEsayDesigner.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "QtEsayDesigner.app" 175 120 \
  --hide-extension "QtEsayDesigner.app" \
  --app-drop-link 425 120 \
  "dist/QtEsayDesigner.dmg" \
  "dist/dmg/"

