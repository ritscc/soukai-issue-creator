def title(page: str, section: str, modification: str) -> str:
    return f"{page}ページ {section} {modification}修正"


def body(author: str, before: str, after: str, url: str) -> str:
    return f"""
@{author}

以下の

```
{before}
```

を

```
{after}
```

に変更してください。

{url}
"""
