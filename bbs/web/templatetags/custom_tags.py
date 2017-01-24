#_*_coding:utf-8_*_
from django import template
from html5lib import HTMLParser
from django.utils.safestring import mark_safe

register = template.Library()
def tree_search(d_dic,comment_obj):
    for k,v_dic in d_dic.items():
        if k == comment_obj.parent_comment:
            d_dic[k][comment_obj] = {}
            return
        else:
            tree_search(d_dic[k],comment_obj)

def generate_comment_html(sub_comment_dic,margin_left_val):
    html = ""
    for k,v_dic in sub_comment_dic.items():
        html += "<div style='margin-left:%spx' class='comment-node'>" % margin_left_val + k.comment + "</div>"
        if v_dic:
            html += generate_comment_html(v_dic,margin_left_val+15)
    return html

@register.simple_tag
def build_comment_tree(comment_list):
    comment_dic = {}
    for comment_obj in comment_list:
        if comment_obj.parent_comment is None:
            comment_dic[comment_obj] = {}
        else:
            tree_search(comment_dic,comment_obj)

    html = "<div class='comment-box'>"
    margin_left = 0
    for k,v in comment_dic.items():
        html += "<div class='comment-node'>" + k.comment + "</div>"
        html += generate_comment_html(v,margin_left+15)
    html += "</div>"
    print(html)
    return html