**準備**
darknetをダウンロード&コンパイル(推奨バージョンではないがCUDA8.0, cudnn6.0で動作確認済み)

https://github.com/AlexeyAB/darknet

Inamgegenerateror_for_yoloは/darknet/に入れておく

**使い方**

1. /items/に認識したい物体名のフォルダを作成し、画像を入れる

2. /backgrounds/に背景画像の入ったフォルダを作成

3. python3 make_obj_names.pyを実行（items/（物体名のフォルダ）/*.pngの名前が学習用に変更し、obj.namesとnames.listが生成される）

画像の名前は0-0000_c0.pngの形式でつけている。

{obj.namesの行番号に対応｝-{同名物体での番号}_{names.listで検索するクラス番号}

4. opu_generator.pyの変数classesに識別したい物体の個数を代入（sets, n_samplesも任意で変更）

5. python3 opu_generator.pyを実行（output/obj/が生成される）

6. bash movefile.sh を実行

7. darknet/data/obj.dataの変数classesやトレーニングデータなどのディレクトリを設定

8. 以下のコマンドで学習を開始

./darknet detector train data/obj.data data/wrs-obj.cfg darknet19_448.conv.23 -map 

9. darknet_rosに利用するのは任意のwightsファイルとcfgファイル、およびnamesファイルの中身に記述されている物体名である。（詳しくはdarknet_rosのREADME参照）

**応用**

(test)

./darknet detector test  data/obj.data  data/wrs-obj.cfg backup/wrs-obj_best.weights data/apple.png 

(yolov2以外のモデルを使いたい場合)

/darknet/cfg/から使いたいモデルのconfigファイルをdarknet/wrs/にコピーする（RoboCup2019ではyolov2-voc.cfg）

yolov2-voc.cfgに以下の変更を加える
・３行目batchのバッチサイズを変更
・４行目subdivisionの値を変更（バッチサイズの画像データのうち、一度に計算する画像の数？）
・２３７行目filtersの値を変更（yolov2の場合、filters = (classes + 5） * 5)
・２４７行目classeに識別したい物体の個数を代入


重みのダウンロード（yolov2）

wget https://pjreddie.com/media/files/darknet19_448.conv.23

（画像を追加したい場合）

items_addに追加したい画像が入ったディレクトリを配置したあと、最初の学習で生成した

train.txt

valid.txt

obj.names

names.list

を同じディレクトリに配置後、python3 add_generator.pyを実行
（output_addに画像が追加されるため、darknetの学習用の画像フォルダに移動させる）

class数が変化しているため、objファイルを適宜変更する

find items_add/ -name "*.png" -print0 | xargs -0 -I {} mv {} ~/darknet/data/obj/

find items_add/ -name "*.txt" -print0 | xargs -0 -I {} mv {} ~/darknet/data/obj/

(GPUを２枚使いたい時(1000回以上学習した重みに対して))
./darknet detector train data/obj.data data/wrs-obj.cfg backup/wrs-obj_last.weight -map max_batches=8000 -gpus 0,1
