import pytest
from managers import ChainManager
from chains import Chain, LLMChain
from utils import logging

@pytest.fixture
def chain_manager():
    return ChainManager()

def test_init(chain_manager):
    assert len(chain_manager.default_chains) == 1
    assert isinstance(chain_manager.default_chains["llm"], LLMChain)
    assert len(chain_manager.custom_chains) == 0

def test_get_chain(chain_manager):
    # Test getting a default chain
    assert chain_manager.get_chain("llm") == chain_manager.default_chains["llm"]

    # Test getting a nonexistent chain
    assert chain_manager.get_chain("nonexistent") is None

    # Test getting a custom chain
    # custom_chain = Chain()
    # chain_manager.custom_chains["custom"] = custom_chain
    # assert chain_manager.get_chain("custom") == custom_chain

def test_get_all_chains(chain_manager):
    # Test getting all chains with only default chains
    all_chains = chain_manager.get_all_chains()
    assert len(all_chains) == 1
    assert all_chains["llm"] == chain_manager.default_chains["llm"]

    # Test getting all chains with custom chains
    # custom_chain = Chain()
    # chain_manager.custom_chains["custom"] = custom_chain
    # all_chains = chain_manager.get_all_chains()
    # assert len(all_chains) == 2
    # assert all_chains["custom"] == custom_chain

def test_get_all_chain_ids(chain_manager):
    # Test getting all chain IDs with only default chains
    chain_ids = chain_manager.get_all_chain_ids()
    assert len(chain_ids) == 1
    assert "llm" in chain_ids

    # Test getting all chain IDs with custom chains
    # custom_chain = Chain()
    # chain_manager.custom_chains["custom"] = custom_chain
    # chain_ids = chain_manager.get_all_chain_ids()
    # assert len(chain_ids) == 2
    # assert "custom" in chain_ids

def test_update_chain(chain_manager):
    # Test updating a default chain
    new_llm_chain = LLMChain()
    chain_manager.update_chain("llm", new_llm_chain)
    assert chain_manager.default_chains["llm"] == new_llm_chain

    # Test updating a custom chain
    # custom_chain = Chain()
    # chain_manager.custom_chains["custom"] = custom_chain
    # new_custom_chain = Chain()
    # chain_manager.update_chain("custom", new_custom_chain)
    # assert chain_manager.custom_chains["custom"] == new_custom_chain

    # Test updating a nonexistent chain
    with pytest.raises(ValueError):
        chain_manager.update_chain("nonexistent", LLMChain())

# def test_create_custom_chain(chain_manager):
#     # Test creating a custom chain
#     chain_manager.create_custom_chain("custom", Chain)
#     assert "custom" in chain_manager.custom_chains

#     # Test creating a custom chain with an existing ID
#     with pytest.raises(ValueError):
#         chain_manager.create_custom_chain("custom", Chain)
#     with pytest.raises(ValueError):
#         chain_manager.create_custom_chain("llm", Chain)

# def test_delete_custom_chain(chain_manager):
#     chain_manager = ChainManager()

#     # Test deleting a nonexistent custom chain (no error should be raised)
#     chain_manager.delete_custom_chain("nonexistent")

#     # Test deleting an existing custom chain
#     custom_chain = Chain()
#     chain_manager.custom_chains["custom"] = custom_chain
#     chain_manager.delete_custom_chain("custom")
#     assert "custom" not in chain_manager.custom_chains
