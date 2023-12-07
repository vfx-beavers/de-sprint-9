from datetime import datetime
from typing import Any, Dict, List
from lib.pg import PgConnect

from .objects import *

class DdsRepository:
    def __init__(self, db: PgConnect) -> None:
        self._db = db

    #хабы
    def h_user_insert(self, user: H_User) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_user (h_user_pk, user_id, load_dt, load_src)
                    values (%(h_user_pk)s, %(user_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(user_id) do nothing;
                    """,
                    {
                        'h_user_pk': user.h_user_pk,
                        'user_id': user.user_id,
                        'load_dt': user.load_dt,
                        'load_src': user.load_src
                    }
                )
                
    def h_product_insert(self, objs: List[H_Product]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.h_product (h_product_pk, product_id, load_dt, load_src)
                    values (%(h_product_pk)s, %(product_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(product_id) do nothing;
                    """,
                    {
                            'h_product_pk': obj.h_product_pk,
                            'product_id': obj.product_id,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src
                        }
                    ) 
    
    def h_category_insert(self, objs: List[H_Category]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.h_category (h_category_pk, category_name, load_dt, load_src)
                    values (%(h_category_pk)s, %(category_name)s, %(load_dt)s, %(load_src)s)
                    on conflict(category_name) do nothing;
                    """,
                    {
                            'h_category_pk': obj.h_category_pk,
                            'category_name': obj.category_name,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src
                        }
                    )

    def h_restaurant_insert(self, restaurant: H_Restaurant) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_restaurant (h_restaurant_pk, restaurant_id, load_dt, load_src)
                    values (%(h_restaurant_pk)s, %(restaurant_id)s, %(load_dt)s, %(load_src)s)
                    on conflict(restaurant_id) do nothing;
                    """,
                    {
                        'h_restaurant_pk': restaurant.h_restaurant_pk,
                        'restaurant_id': restaurant.restaurant_id,
                        'load_dt': restaurant.load_dt,
                        'load_src': restaurant.load_src
                    }
                )

    def h_order_insert(self, order: H_Order) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.h_order (h_order_pk, order_id, load_dt, order_dt, load_src)
                    values (%(h_order_pk)s, %(order_id)s, %(load_dt)s, %(order_dt)s, %(load_src)s)
                    on conflict(order_id) do nothing;
                    """,
                    {
                        'h_order_pk': order.h_order_pk,
                        'order_id': order.order_id,
                        'order_dt': order.order_dt,
                        'load_dt': order.load_dt,
                        'load_src': order.load_src
                    }
                )

    #линки
    def l_order_product_insert(self, objs: List[L_order_product]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.l_order_product (hk_order_product_pk, h_order_pk, h_product_pk, load_dt, load_src)
                    values (%(hk_order_product_pk)s, %(h_order_pk)s, %(h_product_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_order_product_pk) do nothing;
                    """,
                    {
                            'hk_order_product_pk': obj.hk_order_product_pk,
                            'h_product_pk': obj.h_product_pk,
                            'h_order_pk': obj.h_order_pk,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src
                        }
                    )

    def l_product_restaurant_insert(self, objs: List[L_product_restaurant]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.l_product_restaurant (hk_product_restaurant_pk, h_product_pk, h_restaurant_pk, load_dt, load_src)
                    values (%(hk_product_restaurant_pk)s, %(h_product_pk)s, %(h_restaurant_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_product_restaurant_pk) do nothing;
                    """,
                    {
                            'hk_product_restaurant_pk': obj.hk_product_restaurant_pk,
                            'h_restaurant_pk': obj.h_restaurant_pk,
                            'h_product_pk': obj.h_product_pk,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src
                        }
                    )

    def l_product_category_insert(self, objs: List[L_product_category]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.l_product_category (hk_product_category_pk, h_product_pk, h_category_pk, load_dt, load_src)
                    values (%(hk_product_category_pk)s, %(h_product_pk)s, %(h_category_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_product_category_pk) do nothing;
                    """,
                    {
                            'hk_product_category_pk': obj.hk_product_category_pk,
                            'h_product_pk': obj.h_product_pk,
                            'h_category_pk': obj.h_category_pk,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src
                        }
                    )

    def l_order_user_insert(self, l_order_user: L_order_user) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.l_order_user (hk_order_user_pk, h_order_pk, h_user_pk, load_dt, load_src)
                    values (%(hk_order_user_pk)s, %(h_order_pk)s, %(h_user_pk)s, %(load_dt)s, %(load_src)s)
                    on conflict(hk_order_user_pk) do nothing;
                    """,
                    {
                        'hk_order_user_pk': l_order_user.hk_order_user_pk,
                        'h_user_pk': l_order_user.h_user_pk,
                        'h_order_pk': l_order_user.h_order_pk,
                        'load_dt': l_order_user.load_dt,
                        'load_src': l_order_user.load_src
                    }
                )

    #сателлиты
    def s_user_names_insert(self, user_names: S_user_names) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_user_names (h_user_pk, username, userlogin, load_dt, load_src, hk_user_names_hashdiff)
                    values (%(h_user_pk)s, %(username)s, %(userlogin)s, %(load_dt)s, %(load_src)s, %(hk_user_names_hashdiff)s)
                    on conflict(hk_user_names_hashdiff) do nothing;
                    """,
                    {
                        'h_user_pk': user_names.h_user_pk,
                        'username': user_names.username,
                        'userlogin': user_names.userlogin,
                        'load_dt': user_names.load_dt,
                        'load_src': user_names.load_src,
                        'hk_user_names_hashdiff': user_names.hk_user_names_hashdiff
                    }
                )


    def s_product_names_insert(self,objs: List[S_product_names]) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                for obj in objs:
                    cur.execute(
                    """
                    insert into dds.s_product_names (h_product_pk, name, load_dt, load_src, hk_product_names_hashdiff)
                    values (%(h_product_pk)s, %(name)s, %(load_dt)s, %(load_src)s, %(hk_product_names_hashdiff)s)
                    on conflict(hk_product_names_hashdiff) do nothing;
                    """,
                    {
                            'h_product_pk': obj.h_product_pk,
                            'name': obj.name,
                            'load_dt': obj.load_dt,
                            'load_src': obj.load_src,
                            'hk_product_names_hashdiff': obj.hk_product_names_hashdiff
                        }
                    )

    def s_restaurant_names_insert(self, restaurant_names: S_restaurant_names) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_restaurant_names (h_restaurant_pk, name, load_dt, load_src, hk_restaurant_names_hashdiff)
                    values (%(h_restaurant_pk)s, %(name)s, %(load_dt)s, %(load_src)s, %(hk_restaurant_names_hashdiff)s)
                    on conflict(hk_restaurant_names_hashdiff) do nothing;
                    """,
                    {
                        'h_restaurant_pk': restaurant_names.h_restaurant_pk,
                        'name': restaurant_names.name,
                        'load_dt': restaurant_names.load_dt,
                        'load_src': restaurant_names.load_src,
                        'hk_restaurant_names_hashdiff': restaurant_names.hk_restaurant_names_hashdiff
                    }
                )

    def s_order_cost_insert(self, order_cost: S_order_cost) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_order_cost (h_order_pk, cost, payment, load_dt, load_src, hk_order_cost_hashdiff)
                    values (%(h_order_pk)s, %(cost)s, %(payment)s, %(load_dt)s, %(load_src)s, %(hk_order_cost_hashdiff)s)
                    on conflict(hk_order_cost_hashdiff) do nothing;
                    """,
                    {
                        'h_order_pk': order_cost.h_order_pk,
                        'cost': order_cost.cost,
                        'payment': order_cost.payment,
                        'load_dt': order_cost.load_dt,
                        'load_src': order_cost.load_src,
                        'hk_order_cost_hashdiff': order_cost.hk_order_cost_hashdiff
                    }
                )

    def s_order_status_insert(self, order_status: S_order_status) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into dds.s_order_status (h_order_pk, status, load_dt, load_src, hk_order_status_hashdiff)
                    values (%(h_order_pk)s, %(status)s, %(load_dt)s, %(load_src)s, %(hk_order_status_hashdiff)s)
                    on conflict(hk_order_status_hashdiff) do nothing;
                    """,
                    {
                        'h_order_pk': order_status.h_order_pk,
                        'status': order_status.status,
                        'load_dt': order_status.load_dt,
                        'load_src': order_status.load_src,
                        'hk_order_status_hashdiff': order_status.hk_order_status_hashdiff
                    }
                )