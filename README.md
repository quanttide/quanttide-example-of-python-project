# 量潮Python项目示例

## 环境配置

1. 安装 Python 环境：

   前往 [https://www.python.org/](https://www.python.org/) 下载安装 Python (>= 3.10)，然后在命令行中执行：

    ```shell
    pip install pdm
    pdm install
    ```

   若下载缓慢，可换源：

    ```shell
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
    ```

2. 在`项目根目录`下执行以下命令安装依赖项：

   ```shell
   pdm install
   ```

## 运行

1. 在`项目根目录`下执行以下命令：

   ```shell
   pdm run python project_name/__main__.py
   ```

## 示例内容说明

- 针对场景：用以直接运行的`Python`项目，除了`Django`和`Python库`有各自的模板以外，一般情况都可以用。

- 用法：创建`Github`仓库时可以选择为模板，已经创建仓库的可以手动参照调整。

- 需要注意修改的：`pyproject.toml` 和 `README` 中的名称和描述；`project_name` 文件夹重命名为项目名称或史诗名称

- 包含内容：`dynaconf` 配置（`project_name/config.py`）、日志配置（`project_name/__main__.py` 与 `settings.yml`）、`pdm` 配置（`pyproject.toml`、`pdm.lock`，默认依赖 `dynaconf、pytest`）、文档结构（`README`、`CHANGELOG`、`docs`（用户文档））、代码目录结构（`tests`（单元测试）、`integrated_tests`（集成测试））、`.gitignore`

- 备注：

   - `__main__.py` 是其目录下所有代码的唯一统一入口（如有需要可改名），如有其它需单独运行的简单脚本，在项目根目录下创建 `scripts` 文件夹；如有多个不能一起完成的交付目标（里程碑），在项目根目录下新创建文件夹及其自己的 `__main__.py` 等文件

   - 如需跨一级目录（一级目录即项目根目录的下一级）`import` 代码，将`pyproject.toml` 中的 `[tool.pdm] distribution` 改为 `true`，重新执行 `pdm install` 后即可从任意一级目录开始 `import`

   - 要指定环境时，在 `settings.yml` 同目录下创建 `.env` 文件以指定环境，内容如 `DYNACONF_STAGE=prod`

   - 涉及敏感配置时（各类密码密钥、用户名、我们的服务器地址、IP等），在 `settings.yml` 同目录下创建 `.secrets.yml` 文件（`.gitignore` 末尾已添加 `.secrets.*`）以放置敏感配置

   - 有测试数据文件要放时，在 `tests` 或 `integrated_tests` 目录下创建 `sample` 文件夹放置

   - 用户文档有图片时，在 `docs` 目录下创建 `images` 文件夹放置
