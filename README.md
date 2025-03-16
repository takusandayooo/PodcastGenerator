# PDF to ポッドキャスト変換ツール

このツールは、PDFファイルをインプットとして、自然な会話形式のポッドキャストを生成するアプリケーションです。Gemini AIを使用してPDFから会話テキストを抽出し、Edge TTSによって音声合成を行います。

## 機能

- 📄 PDFファイルから会話形式のコンテンツを自動生成
- 🗣️ 2人の話者による自然な対話形式で出力
- 🔊 テキストを高品質な音声に変換
- 📝 JSON形式で会話データを保存
- 🎧 MP3形式のポッドキャストを出力
- 🌐 Webインターフェースでの簡単な操作

## 必要環境

- Python 3.10.12 (3.13.0では動作しません)
- ffmpeg

## インストール方法

### 1. ffmpegのインストール

```bash
brew install ffmpeg
```

### 2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. 環境設定

[`.env.example`](.env.example)をコピーして`.env`ファイルを作成し、Gemini APIキーを設定してください。

```
GOOGLE_API_KEY=あなたのGeminiAPIキー
```

## 使用方法

### Webインターフェースを使用する方法

1. 以下のコマンドでFlaskサーバーを起動します:

```bash
python main.py
```

2. ブラウザで `http://127.0.0.1:5000/` にアクセスします
3. Webインターフェースでファイル選択からPDFをアップロードします
4. 「アップロード」ボタンをクリックして処理を開始します
5. 処理が完了すると、ポッドキャストが自動的に再生されます

### コマンドラインから使用する方法

1. 変換したいPDFファイルを`static/input.pdf`として配置します
2. 以下のコマンドを実行します:

```bash
python main.py
```

3. 処理が完了すると、`static/output.mp3`としてポッドキャストファイルが生成されます

## プロジェクト構成

- [`main.py`](main.py): メイン実行ファイルとFlaskアプリケーション
- [`module/gemini_create_text.py`](module/gemini_create_text.py): PDFからテキスト生成を行うモジュール
- [`module/text_to_speech.py`](module/text_to_speech.py): テキストから音声合成を行うモジュール
- [`templates/index.html`](templates/index.html): PDFアップロード用のWebインターフェース
- [`templates/podcast.html`](templates/podcast.html): ポッドキャスト再生画面
- [`static/data.json`](static/data.json): 生成された会話スクリプト
- [`static/audio`](static/audio): 個別の音声ファイル格納ディレクトリ
- [`static/output.mp3`](static/output.mp3): 最終的なポッドキャスト出力

## 注意事項

- Python 3.10.12で動作確認しています（3.13.0ではエラーが発生します）
- 処理には有効なGemini APIキーが必要です
- PDFの内容によって生成される会話の質が変わります
- APIキーは`.env`ファイルに保存し、Gitリポジトリにはコミットしないでください

## トラブルシューティング

- **エラー: `ModuleNotFoundError`**: `pip install -r requirements.txt`を実行してください
- **音声が生成されない**: ffmpegが正しくインストールされているか確認してください
- **APIエラー**: Gemini APIキーが正しく設定されているか確認してください

## 今後の展望
- より良いtext-to-speechモデルを使用して音声合成の品質を向上
- 重ね合わせ技術を使用して、複数の話者の音声を生成
- ユーザーが話者の性別や声質を選択できるようにする
- 複数言語対応の実装
- 処理速度の最適化
