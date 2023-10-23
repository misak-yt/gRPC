from grpc.tools import protoc
protoc.main(
    (
        '',
        '-I../api/', #protoファイルが入っているディレクトリ
        '--pyi_out=./',
        '--python_out=./', #コード(pb2)の出力ディレクトリ
        '--grpc_python_out=./', #コード(pb2_grpc)の出力ディレクトリ
        'hello.proto', #コンパイルするprotoファイル
    )
)