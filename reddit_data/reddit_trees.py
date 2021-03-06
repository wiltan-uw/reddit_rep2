from reddit_data.data_models import RedditComment
from reddit_data.data_models.reddit_node import RedditNode
from reddit_data.data_sources.data_source import DataSource


class RedditTrees:
    def __init__(self, data_source: DataSource):
        self.data = data_source

    def get_tree_rooted_at(self, parent_comment: RedditComment) -> RedditNode:
        if parent_comment is None:
            return None

        parent_node = RedditNode(parent_comment)
        child_comments = self.data.get_children(parent_comment.id)
        for child_comment in child_comments:
            child_node = self.get_tree_rooted_at(child_comment)
            if child_node is not None:
                parent_node.children.append(self.get_tree_rooted_at(child_comment))

        return parent_node


