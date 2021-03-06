import os
import sys

from mpirical.serialization import deserialize, serialize
from mpirical.tests.utils import mpi_bcast


def test_serialize_mpi_bcast():
    serialized_mpi_bcast = serialize(mpi_bcast)
    if sys.version_info[0] == 2:
        assert isinstance(serialized_mpi_bcast, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_mpi_bcast, bytes)


def test_deserialize_mpi_bcast():
    serialized_mpi_bcast = serialize(mpi_bcast)
    deserialized_mpi_bcast = deserialize(serialized_mpi_bcast)
    assert deserialized_mpi_bcast('x') == mpi_bcast('x')


def test_deserialize_mpi_bcast_to_from_filename():
    filename = 'serialized_mpi_bcast.out'
    serialized_mpi_bcast = serialize(mpi_bcast, file=filename)
    assert serialized_mpi_bcast is None
    assert os.path.exists(filename)
    deserialized_mpi_bcast = deserialize(file=filename)
    assert deserialized_mpi_bcast('x') == mpi_bcast('x')
    os.remove(filename)


def test_deserialize_mpi_bcast_to_from_file():
    filename = 'serialized_mpi_bcast.out'
    with open(filename, 'wb') as f:
        serialized_mpi_bcast = serialize(mpi_bcast, file=f)
    assert serialized_mpi_bcast is None
    assert os.path.exists(filename)
    with open(filename, 'rb') as f:
        deserialized_mpi_bcast = deserialize(file=f)
    assert deserialized_mpi_bcast('x') == mpi_bcast('x')
    os.remove(filename)
