import pytest

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import (
    psycopg2, psycopg2cffi
)
from sqlalchemy.engine.url import URL

from redshift_sqlalchemy import dialect


@pytest.mark.parametrize('name, expected_dialect', [
    ('redshift', psycopg2.dialect),
    ('redshift+psycopg2', psycopg2.dialect),
    ('redshift+psycopg2cffi', psycopg2cffi.dialect),
])
def test_dialect_inherits_from_sqlalchemy_dialect(name, expected_dialect):
    engine = sa.create_engine(URL(
        drivername=name,
    ))

    assert isinstance(engine.dialect, expected_dialect)


@pytest.mark.parametrize('name, expected_dialect', [
    ('redshift', dialect.PsycopgRedshiftDialectMixin),
    ('redshift+psycopg2', dialect.PsycopgRedshiftDialectMixin),
    ('redshift+psycopg2cffi', dialect.PsycopgRedshiftDialectMixin),
])
def test_dialect_inherits_from_redshift_mixin(name, expected_dialect):
    engine = sa.create_engine(URL(
        drivername=name,
    ))

    assert isinstance(engine.dialect, expected_dialect)


@pytest.mark.parametrize('name, expected_dialect', [
    ('redshift', dialect.Psycopg2RedshiftDialect),
    ('redshift+psycopg2', dialect.Psycopg2RedshiftDialect),
    ('redshift+psycopg2cffi', dialect.Psycopg2CFFIRedshiftDialect),
])
def test_dialect_registered_correct_class(name, expected_dialect):
    engine = sa.create_engine(URL(
        drivername=name,
    ))

    assert isinstance(engine.dialect, expected_dialect)
