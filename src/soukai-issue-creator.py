from template import body, title
from issues import load_issues
from github import Github
from envs import envs


def create_issues():
    g = Github(envs["ACCESS_TOKEN"])

    repo = g.get_repo(envs["REPO"])

    commit_hash = repo.get_git_ref(f"tags/{envs['TAG_NAME']}").object.sha

    for issue in load_issues():
        repo.create_issue(
            title=title(
                page=issue["PAGE"],
                section=issue["SECTION"],
                modification=issue["MODIFICATION"],
            ),
            body=body(
                author=issue["AUTHOR"],
                before=issue["BEFORE"],
                after=issue["AFTER"],
                url=issue["URL"].replace(envs["TAG_NAME"], commit_hash),
            ),
            assignee=issue["AUTHOR"],
        )


if __name__ == "__main__":
    create_issues()
