#!/bin/sh
# 创建dmg目录
mkdir -p dist/dmg
# 删除dmg文件夹的文件
rm -r dist/dmg/*
# 复制编译好的app
cp -r "dist/QtEasyDesigner.app" dist/dmg
# 如果dmg文件存在就删除
test -f "dist/QtEasyDesigner.dmg" && rm "dist/QtEasyDesigner.dmg"
create-dmg \
  --volname "QtEasyDesigner" \
  --volicon "QtEasyDesigner.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "QtEasyDesigner.app" 175 120 \
  --hide-extension "QtEasyDesigner.app" \
  --app-drop-link 425 120 \
  "dist/QtEasyDesigner.dmg" \
  "dist/dmg/"

