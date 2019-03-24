import praw
import textwrap

reddit = praw.Reddit(user_agent='persuasion_scraper',
                     client_id='7-RsL44iU7tDdg', client_secret="4bbtPutXKwlyecZO0nO4QTen4g8" )

submission = reddit.submission(url='https://www.reddit.com/r/changemyview/comments/b0n29q/cmv_arguing_to_convince_others_is_a_terrible/')
submission.comments.replace_more(limit=0)

prefix = "COMMENT:"
preferredWidth = 70
wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                               subsequent_indent=' '*len(prefix))

for top_level_comment in submission.comments:
    print(wrapper.fill(top_level_comment.body))