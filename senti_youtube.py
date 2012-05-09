#! /usr/bin/env python
# -*- coding: utf-8 -*-
import warnings,sys,os,argparse
from senti_classifier import senti_classifier
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import gdata.youtube
    import gdata.youtube.service
import urlparse
youtube_service = gdata.youtube.service.YouTubeService()

def ids_from_urls(youtubeurls = []):
    video_ids = []
    for url in youtubeurls:
        url_data = urlparse.urlparse(url)
        query = urlparse.parse_qs(url_data.query)
        video_ids.append(query["v"][0])
    return video_ids

def comments(youtubeurls = []):
    comments = []
    for vid in ids_from_urls(youtubeurls):
        for comment in youtube_service.GetYouTubeVideoCommentFeed(video_id = vid).entry:
            comments.append(comment.content.text)
    return comments

if __name__ == '__main__':
    youtubeurls = ["http://www.youtube.com/watch?v=u1vASMbEEQc"]
    allcomments = comments(youtubeurls)
    print senti_classifier.polarity_scores(allcomments)
