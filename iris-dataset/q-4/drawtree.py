# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:24:27 2016

@author: Vivek Patani
"""
import pickle
from PIL import Image,ImageDraw

data=pickle.load(open("./result/iris.p","rb"))
col=data[0]
print(col)




def getwidth(tree):
	if tree.tb==None and tree.tb==None: return 1
	return getwidth(tree.tb) + getwidth(tree.fb)

def getdepth(tree):
	if tree.tb==None and tree.fb==None: return 0
	return max(getdepth(tree.tb),getdepth(tree.fb))+1

def drawtree(tree,jpeg='tree.jpg',colname=None):
	print("tree")
	col=colname
	w=getwidth(tree)*100
	h=getdepth(tree)*100+  120

	img=Image.new('RGB',(w,h),(255,255,255))
	draw=ImageDraw.Draw(img)

	drawnode(draw,tree,w/2,20,col)
	img.save(jpeg,'JPEG')


def drawnode(draw,tree,x,y,colname=None):
	col=colname
	if tree.results==None:
	    # Get the width of each branch
	    w1=getwidth(tree.fb)*100
	    w2=getwidth(tree.tb)*100

	    # Determine the total space required by this node
	    left=x-(w1+w2)/2
	    right=x+(w1+w2)/2

	    # Draw the condition string
	    draw.text((x-20,y-10),str(col[tree.col])+':'+str(tree.value),(0,0,0))

	    # Draw links to the branches
	    draw.line((x,y,left+w1/2,y+100),fill=(255,0,0))
	    draw.line((x,y,right-w2/2,y+100),fill=(255,0,0))
	    
	    # Draw the branch nodes
	    drawnode(draw,tree.fb,left+w1/2,y+100,col)
	    drawnode(draw,tree.tb,right-w2/2,y+100,col)
	else:
	    txt=' \n'.join(['%s:%d'%v for v in tree.results.items()])
	    draw.text((x-20,y),txt,(0,0,0))