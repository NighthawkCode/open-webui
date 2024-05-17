from peewee import *
from peewee_migrate import Router
from playhouse.db_url import connect
from config import SRC_LOG_LEVELS, DATA_DIR, DATABASE_URL
import os
import logging

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["DB"])

DB = connect(DATABASE_URL)
log.info(f"Connected to a {DB.__class__.__name__} database.")

router = Router(DB, migrate_dir="apps/web/internal/migrations", logger=log)
router.run()
DB.connect(reuse_if_open=True)
