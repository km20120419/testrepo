{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node(object):#定义节点\n",
    "    def _init_(self,elem):\n",
    "        self.elem = elem\n",
    "        self.next = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "class SingleLinkList(object): #定义链表\n",
    "    def _init_(self,node=None):\n",
    "        self._head=node\n",
    "        \n",
    "    def is_empty(self):\n",
    "        return self._head==None\n",
    "    \n",
    "    def length(self):\n",
    "        cur = self._head #cur游标,用来移动遍历节点,一开始_head为起始节点\n",
    "        count = 0  #count用来记录数量\n",
    "        while cur != None:\n",
    "            count += 1  #每遇到一个节点, count+1\n",
    "            cur = cur.next  #cur游标向后移动\n",
    "        return count #当cur=None的时候退出循环,返回count值\n",
    "    \n",
    "    def travel(self):\n",
    "        cur = self._head\n",
    "        while cur != None:\n",
    "            print(cur.elem)\n",
    "            cur = cur.next\n",
    "            \n",
    "    def append(self,item):\n",
    "        node = Node(item)\n",
    "        if self.is_empty():  #判断链表是否为空? \n",
    "            self._head = node  #如果为空,那么_head直接指向新的节点node就可以了\n",
    "            cur = self._head\n",
    "            while cur.next != None:\n",
    "                cur = cur.next\n",
    "            cur.next = node\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Node() takes no arguments",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-3ac0d96724ce>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnode\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mNode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0msing_obj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSingleLinkList\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0msingle_obj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtravel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Node() takes no arguments"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'SingleLinkList' object has no attribute '_head'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-48d5c4066ab6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mll\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSingleLinkList\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mll\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_empty\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-25-4b67bb0e0400>\u001b[0m in \u001b[0;36mis_empty\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m      3\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_head\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mnode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mis_empty\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_head\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mlength\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m         \u001b[0mcur\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_head\u001b[0m \u001b[1;31m#cur游标,用来移动遍历节点,一开始_head为起始节点\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'SingleLinkList' object has no attribute '_head'"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    ll = SingleLinkList()\n",
    "    print(ll.is_empty())\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
