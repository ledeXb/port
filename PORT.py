�
    �pd�  �                   �d  � d dl Z d dlZd dlZ ej        d�  �         d dlT d dlmZ  ej        d�  �          ed�  �          ed�  �        Z ej	        �   �         Z
 edez  �  �          ed�  �         	  edd	�  �        D ]�Z e j         e j        e j        �  �        Ze�                    ej        �  �        d k    r9	  e j        e�  �        Zn# e j        $ r d
ZY nw xY w e dee�  �        �  �          ej	        �   �         Zee
z
  Z�� edez  �  �         dS # e$ r  ed�  �         Y dS w xY w)�    N�clear)�*)�datetimea[   [92m
 _____   _____   _____    _____       __    __  _____  
|  _  \ /  _  \ |  _  \  |_   _|      \ \  / / |  _  \ 
| |_| | | | | | | |_| |    | |         \ \/ /  | |_| | 
|  ___/ | | | | |  _  /    | |          }  {   |  _  { 
| |     | |_| | | | \ \    | |         / /\ \  | |_| | 
|_|     \_____/ |_|  \_\   |_|        /_/  \_\ |_____/ 
[0mz===> ENTER YOUR IP TO START: z#Scanning Start.. %s pleease wait.. �   i�  zUnKnown ServicezPort %s Open Service:%s %zScanning completed on %szSee You Soon....!)�socket�sys�os�system�timer   �print�input�ip�now�tl�sleep�range�port�AF_INRT�SOCK_STREAM�s�
connect_ex�getservbyport�serv�error�t2�t3�KeyboardInterrupt� �    �PORT XB/PORT.py�<module>r!      s�  �� ���� 
�
�
�
� 	�	�	�	� 	��	�7� � � � � � � � � � � � � � 	��	�7� � � � �� � � � � 	�5�
)�*�*���8�<�>�>�� ��+�R�/� 0� 0� 0� ��a�������a���� 
� 
��
�&�-���v�'9�
:�
:���<�<���"�"�A�%�%�'�)�V�)�$�/�/�����<� '� '� '�&����'�����E�.�.�t�D�9�9�:�:�:��8�<�>�>���b�5���	�E�%�b�(�)�)�)�)�)��� � � �	�E�
����������s7   �6AD �>C�D �C�D �C�;D �D/�.D/