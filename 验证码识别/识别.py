import logging
import ddddocr

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def perform_ocr(image_path):
    try:
        # 创建 OCR 对象，关闭广告显示
        ocr = ddddocr.DdddOcr(show_ad=False)
        try:
            # 以二进制模式打开图像文件
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            # 进行 OCR 识别
            result = ocr.classification(img_bytes)
            return result
        except FileNotFoundError:
            logging.error(f"文件 {image_path} 未找到，请检查文件路径。")
        except Exception as e:
            logging.error(f"图像识别时发生未知错误: {e}")
    except ModuleNotFoundError:
        logging.error("'ddddocr' 库未安装，请使用 'pip install ddddocr' 进行安装。")
    return None


if __name__ == "__main__":
    image_path = '图片/1.png'
    result = perform_ocr(image_path)
    if result is not None:
        print(result)
