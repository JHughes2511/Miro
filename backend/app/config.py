import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # LLM配置（支持 OpenAI SDK 格式的任意 LLM API）
    LLM_API_KEY = os.environ.get('LLM_API_KEY', '')
    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://dashscope.aliyuncs.com/compatible-mode/v1')
    LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'qwen-plus')
    
    # 可选：加速 LLM 配置（用于实体提取等批量处理场景）
    LLM_BOOST_API_KEY = os.environ.get('LLM_BOOST_API_KEY', '')
    LLM_BOOST_BASE_URL = os.environ.get('LLM_BOOST_BASE_URL', '')
    LLM_BOOST_MODEL_NAME = os.environ.get('LLM_BOOST_MODEL_NAME', '')
    
    # ZEP配置
    ZEP_API_KEY = os.environ.get('ZEP_API_KEY', '')

    # 文件上传配置
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx', 'md', 'csv', 'json'}
    
    # OASIS模拟配置
    OASIS_SIMULATION_DATA_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 
        'uploads', 
        'simulations'
    )
