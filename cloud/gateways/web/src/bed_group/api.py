from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from src.bed import schemas as web_bed_schemas
from src.bed_group import schemas as web_bed_group_schemas
from src.bed_group import services as bed_group_services
from src.common.responses import FastJSONResponse
from src.common.schemas import base as common_schemas

api = APIRouter(default_response_class=FastJSONResponse)


@api.post(
    "/bed-group/batch",
    responses={
        status.HTTP_200_OK: {"model": web_bed_group_schemas.WebBedGroupResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="batch-create-bed-groups",
    description=(
        "Create multiple bed groups in a single request. This is ideal for bulk creation when "
        "establishing new bed groupings for different use cases or locations."
    ),
)
async def batch_create_bed_groups(
    payload: web_bed_group_schemas.WebBedGroupCreateResources,
    bed_service: bed_group_services.BedGroupService = Depends(),
) -> FastJSONResponse:
    bed_group = await bed_service.batch_create_bed_groups(payload)
    return FastJSONResponse(bed_group)


@api.put(
    "/bed-group/batch",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": {}},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="batch-create-or-update-bed-groups",
    description=(
        "Create or update multiple bed groups in a single operation. "
        "Use this endpoint to either add new bed groups or update existing ones in bulk, "
        "ensuring the groupings are up-to-date."
    ),
)
async def batch_create_or_update_bed_groups(
    payload: web_bed_group_schemas.WebBatchCreateOrUpdateBedGroup,
    bed_service: bed_group_services.BedGroupService = Depends(),
) -> Response:
    await bed_service.batch_create_or_update_bed_groups(payload)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api.delete(
    "/bed-group/batch",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": {}},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="batch-delete-bed-groups",
    description=(
        "Remove multiple bed groups in a single request. "
        "This operation is useful for batch deletions when bed groups "
        "are no longer required or are being restructured."
    ),
)
async def batch_delete_bed_groups(
    payload: web_bed_group_schemas.WebBedGroupBatchDelete,
    bed_service: bed_group_services.BedGroupService = Depends(),
) -> Response:
    await bed_service.batch_delete_bed_groups(payload)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api.get(
    "/bed-group",
    responses={
        status.HTTP_200_OK: {"model": web_bed_group_schemas.WebBedGroupResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="get-bed-group-list",
    response_class=FastJSONResponse,
    description=(
        "Retrieve a list of all bed groups. "
        "This can be used to get an overview of existing bed groups, "
        "their configurations, and related data."
    ),
)
async def get_bed_group_list(
    bed_group_service: bed_group_services.BedGroupService = Depends(),
) -> FastJSONResponse:
    bed_groups = await bed_group_service.get_bed_groups()
    return FastJSONResponse(bed_groups)


@api.put(
    "/bed-group/{group_id:uuid}/beds",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": {}},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="assign-bed-to-a-group",
    description=(
        "Add or update beds within an existing bed group. "
        "This allows administrators to modify the bed assignments in a specific "
        "group by associating or updating beds based on their group ID."
    ),
)
async def assign_beds_to_a_group(
    payload: web_bed_group_schemas.WebAssignBedsToGroup,
    group_id: UUID,
    bed_group_service: bed_group_services.BedGroupService = Depends(),
) -> Response:
    assign_beds = web_bed_group_schemas.WebAssignBeds.model_construct(
        group_id=group_id, bed_ids=payload.bed_ids
    )
    assign_beds_batch = web_bed_group_schemas.WebBatchAssignBeds.model_construct(
        resources=[assign_beds]
    )
    await bed_group_service.batch_assign_beds(assign_beds_batch)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api.put(
    "/bed-group/beds/batch",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": {}},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="batch-assign-bed-to-a-group",
    description="Assign beds across one or more bed groups in a single batch request.",
)
async def batch_assign_beds(
    payload: web_bed_group_schemas.WebBatchAssignBeds,
    bed_group_service: bed_group_services.BedGroupService = Depends(),
) -> Response:
    await bed_group_service.batch_assign_beds(payload)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api.get(
    "/bed-group/{bed_group_id:uuid}/beds",
    responses={
        status.HTTP_200_OK: {"model": web_bed_schemas.WebBedResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_404_NOT_FOUND: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="get-assigned-bed-for-group",
    response_class=FastJSONResponse,
    description=(
        "Retrieve the list of beds associated with a specific bed group. "
        "This endpoint is helpful for viewing which beds belong to which group."
    ),
)
async def get_bed_group_beds(
    bed_group_id: UUID,
    bed_group_service: bed_group_services.BedGroupService = Depends(),
) -> FastJSONResponse:
    beds = await bed_group_service.get_assigned_beds_for_group(bed_group_id)
    return FastJSONResponse(beds)


@api.get(
    "/bed-group/{bed_group_id:uuid}/alerts",
    responses={
        status.HTTP_200_OK: {"model": web_bed_group_schemas.WebBedGroupAlertResources},
        status.HTTP_401_UNAUTHORIZED: {"model": {}},
        status.HTTP_403_FORBIDDEN: {"model": {}},
        status.HTTP_404_NOT_FOUND: {"model": {}},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": common_schemas.ErrorSchema},
    },
    operation_id="get-bed-group-observations",
    response_class=FastJSONResponse,
    description="Get patient alerts for patients assigned to a bed in the requested bed group.",
)
async def get_bed_group_observations(
    bed_group_id: UUID,
    bed_group_service: bed_group_services.BedGroupService = Depends(),
) -> FastJSONResponse:
    bed_group_observations = await bed_group_service.get_bed_group_observations(bed_group_id)
    return FastJSONResponse(bed_group_observations)
