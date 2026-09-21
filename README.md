# shiyan1 · 学生成绩统计工具

岗位实践 实验一（代码和项目管理软件）的练习项目。

用来演示 Git 的本地仓库、提交、`.gitignore`、远程仓库、分支管理与协作流程。

## 功能

- 读取一串成绩，统计平均分、最高分、最低分
- 按等级（优 / 良 / 中 / 及格 / 不及格）分类统计人数
- 支持从 CSV 文件读取成绩

## 目录结构

```
shiyan1/
├── README.md
├── .gitignore
├── src/
│   └── grade_stats.py      # 主要功能模块
├── tests/
│   └── test_grade_stats.py # 单元测试
└── docs/
    └── 使用说明.md
```

## 运行测试

```powershell
python -m unittest discover -s tests -v
```

## 版本

- v0.1 初始版本

## 作者

吴子牛 2024041009
