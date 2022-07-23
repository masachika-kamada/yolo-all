def thresh(param):
    return "-thresh " + str(param)


def iou_thresh(param):
    return "-iou_thresh " + str(param)


def camera(index):
    return "-c " + str(index)


def movie_output(file_name):
    return "-out_filename " + file_name


def prefix(basename):
    return "-prefix " + basename


def multi_input(file_name):
    return "< " + file_name


def save_result(file_name):
    return "> " + file_name


def json_output(file_name):
    return "-out " + file_name


def make_commands(dir_ref, darknet_dir, yolo_version):
    darknet = "darknet detector"
    data_file = dir_ref + "/obj.data"
    cfg_file_train = dir_ref + f"/yolov{yolo_version}_train.cfg"
    cfg_file_test = dir_ref + f"/yolov{yolo_version}_test.cfg"
    weights_file = dir_ref + "/backup/yolo-obj_****.weights"
    start_weights = "yolov4.conv.137" if yolo_version == 4 else "darknet53.conv.74"
    start_weights = darknet_dir + "/weights/" + start_weights
    files = " ".join([data_file, cfg_file_test, weights_file])

    train = " ".join([darknet, "train", data_file, cfg_file_train, start_weights])
    test = " ".join([darknet, "test", files])
    demo = " ".join([darknet, "demo", files])
    mAP = " ".join([darknet, "map", files])

    # options
    ext_output = "-ext_output"  # コマンドプロンプト上に検出場所を出力
    dont_show = "-dont_show"
    save_labels = "-save_labels"
    graph = "-map"

    commands = "\n".join([

        "学習",
        " ".join([train, graph]),

        "\n画像からの認識(コマンドプロンプトへBBox位置の出力あり)",
        " ".join([test, ext_output, "dog.jpg"]),

        "\n動画からの認識",
        " ".join([demo, ext_output, "test.mp4"]),

        "\nwebカメラを使ったデモ(カメラ番号)",
        " ".join([demo, camera(0)]),

        "\n動画からの認識(認識結果を動画に書き出し)",
        " ".join([demo, "test.mp4", movie_output(dir_ref + "/res.avi")]),

        "\n動画からの認識(認識結果をフレームごとに画像として書き出し)",
        " ".join([demo, "test.mp4", prefix(dir_ref + "/results/img")]),

        "\ntxtファイル内の画像を一括認識し結果をjsonファイルに保存",
        " ".join([test, ext_output, dont_show, json_output(dir_ref + "/result.json"), multi_input(dir_ref + "/train.txt")]),

        "\ntxtファイル内の画像を一括認識し結果をtxtファイルに保存",
        " ".join([test, ext_output, dont_show, multi_input(dir_ref + "train.txt"), save_result(dir_ref + "/result.txt")]),

        "\n疑似ラベリング(txtファイル内の画像を一括認識し、ラベルをtrainデータ形式で保存)",
        " ".join([test, thresh(0.25), dont_show, save_labels, multi_input(dir_ref + "/new_train.txt")]),

        "\nmAP@IoU=50",
        " ".join([mAP]),

        "\nmAP@IoU=75",
        " ".join([mAP, iou_thresh(0.75)]),

        "\n評価",
        " ".join([mAP, save_result(dir_ref + "result_****.txt")])
    ])

    return commands
