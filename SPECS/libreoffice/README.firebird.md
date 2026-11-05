# Firebird 5 backend

Base uses Firebird 5 for embedded databases. New databases use ODS 13.1.

The SDBC driver requests result representations supported by Base:
INT128 results are returned as BIGINT, DECFLOAT as DOUBLE PRECISION,
and zoned time/timestamp results as their non-zoned forms.
Values outside the integer range cannot be fetched; conversion from
DECFLOAT can lose decimal precision. These settings apply only to
Base connections and leave other applications' connections unchanged.
