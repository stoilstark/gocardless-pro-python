# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers

@responses.activate
def test_mandates_create():
    fixture = helpers.load_fixture('mandates')['create']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.create(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_mandates_list():
    fixture = helpers.load_fixture('mandates')['list']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.list(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.Mandate)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.created_at for r in response],
                  [b.get('created_at') for b in body])
    assert_equal([r.id for r in response],
                  [b.get('id') for b in body])
    assert_equal([r.links for r in response],
                  [b.get('links') for b in body])
    assert_equal([r.metadata for r in response],
                  [b.get('metadata') for b in body])
    assert_equal([r.next_possible_charge_date for r in response],
                  [b.get('next_possible_charge_date') for b in body])
    assert_equal([r.reference for r in response],
                  [b.get('reference') for b in body])
    assert_equal([r.scheme for r in response],
                  [b.get('scheme') for b in body])
    assert_equal([r.status for r in response],
                  [b.get('status') for b in body])

@responses.activate
def test_mandates_get():
    fixture = helpers.load_fixture('mandates')['get']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.get(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_mandates_update():
    fixture = helpers.load_fixture('mandates')['update']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.update(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_mandates_cancel():
    fixture = helpers.load_fixture('mandates')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.cancel(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_mandates_reinstate():
    fixture = helpers.load_fixture('mandates')['reinstate']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.reinstate(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert_is_instance(response, resources.Mandate)

    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.next_possible_charge_date, body.get('next_possible_charge_date'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))
