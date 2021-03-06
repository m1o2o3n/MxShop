# Generated by Django 2.0 on 2018-08-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20170826_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=None, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=None, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=None, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=None, related_name='images', to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=None, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=None, related_name='goods', to='goods.Goods'),
        ),
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table='goods_goodsbrand',
        ),
    ]
