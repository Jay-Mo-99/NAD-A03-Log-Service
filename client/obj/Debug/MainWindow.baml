   M S B A M L   `   `   `  ����A  =client, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:clientclient  5   	       client.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   &localclr-namespace:client     5   	     � Title$  
MainWindow��5   	   $	��450��6   $	��800��6)   .��5	      �  � ColumnDefinitions 5
   
   �� 5      $��0* �6   �� 5      .+�5   
   �� -   5         ��Name$ txt_IP��5      $
��Left=�6"   $��	93,51,0,0q�6=    �� TextWrapping$
 Wrap=�6P   $��10.169.92.10��6d   $	��Top=�6x   $	��255��6�    J� RenderTransformOrigin$ -0.158,-0.577&�6�   $��2��6�   �� 5   
   -   5        $ txt_Port��5      $
��Left=�6$   $��
451,52,0,0q�6?   $
 Wrap=�6S   $
��8000��6g   $	��Top=�6s   $	��120��6�   $ -0.158,-0.577&�6�   $��2��6�   �� 5   
   -   5        $ txt_Msg��5      $
��Left=�6#   $��
93,106,0,0q�6>   $
 Wrap=�6R   $	��Top=�6f   $	��478��6~   $ -0.158,-0.577&�6�   $��2��6�   �� 5   
   $��IP/Host��6   $��2��6"   $
��Left=�66   $��	22,47,0,0q�6Q   $	��Top=�6d   $ 0.016,0.055&�6|   �� 5   
   $
��Port��6   $��2��6   $
��Left=�63   $��
400,47,0,0q�6N   $	��Top=�6b   $ 0.016,0.055&�6z   �� 5   
   $��Message��6   $��2��6"   $
��Left=�66   $��
22,102,0,0q�6Q   $	��Top=�6e   $ 0.016,0.055&�6}   �� 5   
   -   5         ��Name$ btn_Connect��5      $��Connect��6&   $��2��68   $
��Left=�6L   $��
625,53,0,0q�6g   $	��Top=�6{   $ -0.313,0.643&�6�   $��62��6�   6�   �� 5   
   -   5        $ btn_Disconnect��5      $��
Disconnect��6)   $��2��6>   $
��Left=�6R   $��
704,52,0,0q�6m   $	��Top=�6�   6�   �� 5   
   -   5        $ btn_Send��5      $
��Send��6#   $��2��62   $
��Left=�6F   $��625,104,0,0q�6a   $	��Top=�6v   $	��141��6�   $ 0.144,-0.008&�6�   6�   �� 5   
   -   5         ��Name$ listBox_Display��5      $��2��6+   $��24,170,229,42q�6j   5      5      