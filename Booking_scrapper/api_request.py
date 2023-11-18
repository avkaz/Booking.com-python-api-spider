import re
from datetime import timedelta

class APIRequest:
    def __init__(self):
        self.url = "https://www.booking.com/dml/graphql"

    def get_querystring(self, checkin_date):
        checkout_date = checkin_date + timedelta(days=1)
        querystring = {"aid": "397594",
                   "label": "gog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB",
                   "sid": "c0b14234663a36fc66ae8b417d55092c", "sb": "1", "sb_lp": "1", "src": "city", "src_elem": "sb",
                   "error_url": "https://www.booking.com/city/cz/prague.cs.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB&sid=c0b14234663a36fc66ae8b417d55092c&inac=0&&",
                   "ss": "Praha", "is_ski_area": "0", "ssne": "Praha", "ssne_untouched": "Praha", "city": "-553173",
                   "checkin_year": checkin_date.year, "checkin_month": checkin_date.month, "checkin_monthday": checkin_date.day, "checkout_year": checkout_date.year,
                   "checkout_month": checkout_date.month, "checkout_monthday": checkout_date.day, "flex_window": "0", "efdco": "1",
                   "group_adults": "2", "group_children": "0", "no_rooms": "1", "b_h4u_keep_filters": "",
                   "from_sf": "1", "lang": "cs"}
        return querystring

    def get_payload(self, offset, checkin_date):
        checkout_date = checkin_date + timedelta(days=1)
        payload = {"operationName": "FullSearch",
        "variables": {
            "input": {
                "acidCarouselContext": None,
                "childrenAges": [],
                "dates": {
                    "checkin": checkin_date.strftime("%Y-%m-%d"),
                    "checkout": checkout_date.strftime("%Y-%m-%d")
                },
                "doAvailabilityCheck": False,
                "encodedAutocompleteMeta": None,
                "enableCampaigns": True,
                "filters": {},
                "forcedBlocks": None,
                "location": {
                    "searchString": "Praha",
                    "destType": "CITY",
                    "destId": -553173
                },
                "metaContext": {
                    "metaCampaignId": 0,
                    "externalTotalPrice": None,
                    "feedPrice": None,
                    "hotelCenterAccountId": None,
                    "rateRuleId": None,
                    "dragongateTraceId": None,
                    "pricingProductsTag": None
                },
                "nbRooms": 1,
                "nbAdults": 2,
                "nbChildren": 0,
                "showAparthotelAsHotel": True,
                "needsRoomsMatch": False,
                "optionalFeatures": {
                    "forceArpExperiments": True,
                    "testProperties": False
                },
                "pagination": {
                    "rowsPerPage": 100,
                    "offset": offset
                },
                "rawQueryForSession": f"/searchresults.cs.html?label=gog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB&sid=c0b14234663a36fc66ae8b417d55092c&aid=397594&sb=1&sb_lp=1&src=city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcity%2Fcz%2Fprague.cs.html%3Faid%3D397594%26label%3Dgog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB%26sid%3Dc0b14234663a36fc66ae8b417d55092c%26inac%3D0%26%26&ss=Praha&is_ski_area=0&ssne=Praha&ssne_untouched=Praha&city=-553173&checkin_year={checkin_date.year}&checkin_month={checkin_date.month}&checkin_monthday={checkin_date.day}&checkout_year={checkout_date.year}&checkout_month={checkout_date.month}&checkout_monthday={checkout_date.day}&flex_window=0&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset={offset}",
                "referrerBlock": None,
                "sorters": {
                    "selectedSorter": None,
                    "referenceGeoId": None,
                    "tripTypeIntentId": None
                },
                "travelPurpose": 2,
                "seoThemeIds": [],
                "useSearchParamsFromSession": True,
                "merchInput": {"testCampaignIds": []}
            },
            "geniusVipUI": {
                "enableEnroll": True,
                "page": "SEARCH_RESULTS"
            },
            "merchIntExp": True
        },
        "extensions": {},
        "query": """query FullSearch($input: SearchQueryInput!, $geniusVipUI: GeniusVipUIsInput, $merchIntExp: Boolean!) {
        searchQueries {
            search(input: $input) {
        ...
    FullSearchFragment
    __typename
    }
    __typename
    }
    geniusVipEnrolledProgram(input: $geniusVipUI) {
        ...
    geniusVipEnrolledProgram
    __typename
    }
    }

    fragment
    FullSearchFragment
    on
    SearchQueryOutput
    {
        banners
    {
        ...
    Banner
    __typename
    }
    breadcrumbs
    {
        ...
    on
    SearchResultsBreadcrumb
    {
        ...
    SearchResultsBreadcrumb
    __typename
    }
    ...
    on
    LandingPageBreadcrumb
    {
        ...
    LandingPageBreadcrumb
    __typename
    }
    __typename
    }
    carousels
    {
        ...
    Carousel
    __typename
    }
    destinationLocation
    {
        ...
    DestinationLocation
    __typename
    }
    entireHomesSearchEnabled
    dateFlexibilityOptions
    {
        enabled
    __typename
    }
    filters
    {
        ...
    FilterData
    __typename
    }
    appliedFilterOptions
    {
        ...
    FilterOption
    __typename
    }
    recommendedFilterOptions
    {
        ...
    FilterOption
    __typename
    }
    pagination
    {
        nbResultsPerPage
    nbResultsTotal
    __typename
    }
    tripTypes
    {
        ...
    TripTypesData
    __typename
    }
    results
    {
        ...
    BasicPropertyData
    ...MatchingUnitConfigurations
    ...PropertyBlocks
    ...BookerExperienceData
    priceDisplayInfoIrene
    {
        ...
    PriceDisplayInfoIrene
    __typename
    }
    licenseDetails
    {
        nextToHotelName
    __typename
    }
    inferredLocationScore
    trackOnView
    {
        experimentTag
    __typename
    }
    topPhotos
    {
        highResUrl
    {
        relativeUrl
    __typename
    }
    lowResUrl
    {
        relativeUrl
    __typename
    }
    highResJpegUrl
    {
        relativeUrl
    __typename
    }
    lowResJpegUrl
    {
        relativeUrl
    __typename
    }
    __typename
    }
    __typename
    }
    searchMeta
    {
        ...
    SearchMetadata
    __typename
    }
    sorters
    {
        option
    {
        ...
    SorterFields
    __typename
    }
    __typename
    }
    oneOfThreeDeal
    {
        ...
    OneOfThreeDeal
    __typename
    }
    zeroResultsSection
    {
        ...
    ZeroResultsSection
    __typename
    }
    rocketmilesSearchUuid
    previousSearches
    {
        ...
    PreviousSearches
    __typename
    }
    frontierThemes
    {
        ...
    FrontierThemes
    __typename
    }
    merchComponents @ include( if: $merchIntExp) {
        ...
    MerchRegionIrene
    __typename
    }
    __typename
    }

    fragment
    BasicPropertyData
    on
    SearchResultProperty
    {
        acceptsWalletCredit
    basicPropertyData
    {
        accommodationTypeId
    id
    isTestProperty
    location
    {
        address
    city
    countryCode
    __typename
    }
    pageName
    ufi
    photos
    {
        main
    {
        highResUrl
    {
        relativeUrl
    __typename
    }
    lowResUrl
    {
        relativeUrl
    __typename
    }
    highResJpegUrl
    {
        relativeUrl
    __typename
    }
    lowResJpegUrl
    {
        relativeUrl
    __typename
    }
    __typename
    }
    __typename
    }
    reviewScore: reviews
    {
        score: totalScore
        reviewCount: reviewsCount
        totalScoreTextTag {
            translation
        __typename
    }
    showScore
    secondaryScore
    secondaryTextTag
    {
        translation
    __typename
    }
    showSecondaryScore
    __typename
    }
    externalReviewScore: externalReviews
    {
        score: totalScore
        reviewCount: reviewsCount
        showScore
            totalScoreTextTag {
        translation
        __typename
    }
    __typename
    }
    alternativeExternalReviewsScore: alternativeExternalReviews
    {
        score: totalScore
        reviewCount: reviewsCount
        showScore
            totalScoreTextTag {
        translation
        __typename
    }
    __typename
    }
    starRating
    {
        value
    symbol
    caption
    {
        translation
    __typename
    }
    tocLink
    {
        translation
    __typename
    }
    showAdditionalInfoIcon
    __typename
    }
    isClosed
    paymentConfig
    {
        installments
    {
        minPriceFormatted
    maxAcceptCount
    __typename
    }
    __typename
    }
    __typename
    }
    badges
    {
        caption
    {
        translation
    __typename
    }
    closedFacilities
    {
        startDate
    endDate
    __typename
    }
    __typename
    }
    customBadges
    {
        showIsWorkFriendly
    showParkAndFly
    showSkiToDoor
    showBhTravelCreditBadge
    showOnlineCheckinBadge
    __typename
    }
    description
    {
        text
    __typename
    }
    displayName
    {
        text
    translationTag
    {
        translation
    __typename
    }
    __typename
    }
    geniusInfo
    {
        benefitsCommunication
    {
        header
    {
        title
    __typename
    }
    items
    {
        title
    __typename
    }
    __typename
    }
    geniusBenefits
    geniusBenefitsData
    {
        hotelCardHasFreeBreakfast
    hotelCardHasFreeRoomUpgrade
    sortedBenefits
    __typename
    }
    showGeniusRateBadge
    __typename
    }
    location
    {
        displayLocation
    mainDistance
    publicTransportDistanceDescription
    skiLiftDistance
    beachDistance
    nearbyBeachNames
    beachWalkingTime
    geoDistanceMeters
    __typename
    }
    mealPlanIncluded
    {
        mealPlanType
    text
    __typename
    }
    persuasion
    {
        autoextended
    geniusRateAvailable
    highlighted
    preferred
    preferredPlus
    showNativeAdLabel
    nativeAdId
    nativeAdsCpc
    nativeAdsTracking
    bookedXTimesMessage
    sponsoredAdsData
    {
        isDsaCompliant
    legalEntityName
    sponsoredAdsDesign
    __typename
    }
    __typename
    }
    policies
    {
        showFreeCancellation
    showNoPrepayment
    enableJapaneseUsersSpecialCase
    __typename
    }
    ribbon
    {
        ribbonType
    text
    __typename
    }
    recommendedDate
    {
        checkin
    checkout
    lengthOfStay
    __typename
    }
    showGeniusLoginMessage
    showPrivateHostMessage
    hostTraderLabel
    soldOutInfo
    {
        isSoldOut
    messages
    {
        text
    __typename
    }
    alternativeDatesMessages
    {
        text
    __typename
    }
    __typename
    }
    nbWishlists
    visibilityBoosterEnabled
    showAdLabel
    isNewlyOpened
    propertySustainability
    {
        isSustainable
    tier
    {
        type
    __typename
    }
    facilities
    {
        id
    __typename
    }
    certifications
    {
        name
    __typename
    }
    chainProgrammes
    {
        chainName
    programmeName
    __typename
    }
    levelId
    __typename
    }
    seoThemes
    {
        caption
    __typename
    }
    relocationMode
    {
        distanceToCityCenterKm
    distanceToCityCenterMiles
    distanceToOriginalHotelKm
    distanceToOriginalHotelMiles
    phoneNumber
    __typename
    }
    bundleRatesAvailable
    recommendedDatesLabel
    __typename
    }

    fragment
    Banner
    on
    Banner
    {
        name
    type
    isDismissible
    showAfterDismissedDuration
    position
    requestAlternativeDates
    merchId @ include( if: $merchIntExp)
    title
    {
        text
    __typename
    }
    imageUrl
    paragraphs
    {
        text
    __typename
    }
    metadata
    {
        key
    value
    __typename
    }
    pendingReviewInfo
    {
        propertyPhoto
    {
        lowResUrl
    {
        relativeUrl
    __typename
    }
    lowResJpegUrl
    {
        relativeUrl
    __typename
    }
    __typename
    }
    propertyName
    urlAccessCode
    __typename
    }
    nbDeals
    primaryAction
    {
        text
    {
        text
    __typename
    }
    action
    {
        name
    context
    {
        key
    value
    __typename
    }
    __typename
    }
    __typename
    }
    secondaryAction
    {
        text
    {
        text
    __typename
    }
    action
    {
        name
    context
    {
        key
    value
    __typename
    }
    __typename
    }
    __typename
    }
    iconName
    flexibleFilterOptions
    {
        optionId
    filterName
    __typename
    }
    trackOnView
    {
        type
    experimentHash
    value
    __typename
    }
    dateFlexQueryOptions
    {
        text
    {
        text
    __typename
    }
    action
    {
        name
    context
    {
        key
    value
    __typename
    }
    __typename
    }
    isApplied
    __typename
    }
    __typename
    }

    fragment
    Carousel
    on
    Carousel
    {
        aggregatedCountsByFilterId
    carouselId
    position
    contentType
    hotelId
    name
    soldoutProperties
    priority
    themeId
    title
    {
        text
    __typename
    }
    slides
    {
        captionText
    {
        text
    __typename
    }
    name
    photoUrl
    subtitle
    {
        text
    __typename
    }
    type
    title {
        text
    __typename
    }
    action
    {
        context
    {
        key
    value
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    DestinationLocation
    on
    DestinationLocation
    {
        name
    {
        text
    __typename
    }
    inName
    {
        text
    __typename
    }
    countryCode
    __typename
    }

    fragment
    FilterData
    on
    Filter
    {
        trackOnView
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClick
    {
        type
    experimentHash
    value
    __typename
    }
    name
    field
    category
    filterStyle
    title
    {
        text
    translationTag
    {
        translation
    __typename
    }
    __typename
    }
    subtitle
    options
    {
        trackOnView
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClick
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnSelect
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnDeSelect
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnViewPopular
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClickPopular
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnSelectPopular
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnDeSelectPopular
    {
        type
    experimentHash
    value
    __typename
    }
    ...
    FilterOption
    __typename
    }
    filterLayout
    {
        isCollapsable
    collapsedCount
    __typename
    }
    stepperOptions
    {
        min
    max
    default
    selected
    title
    {
        text
    translationTag
    {
        translation
    __typename
    }
    __typename
    }
    field
    labels
    {
        text
    translationTag
    {
        translation
    __typename
    }
    __typename
    }
    trackOnView
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClick
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnSelect
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnDeSelect
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClickDecrease
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnClickIncrease
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnDecrease
    {
        type
    experimentHash
    value
    __typename
    }
    trackOnIncrease
    {
        type
    experimentHash
    value
    __typename
    }
    __typename
    }
    sliderOptions
    {
        min
    max
    minSelected
    maxSelected
    minPriceStep
    minSelectedFormatted
    currency
    histogram
    selectedRange
    {
        translation
    __typename
    }
    title
    __typename
    }
    sliderOptionsPerStay
    {
        min
    max
    minSelected
    maxSelected
    minPriceStep
    minSelectedFormatted
    currency
    histogram
    selectedRange
    {
        translation
    __typename
    }
    title
    __typename
    }
    __typename
    }

    fragment
    FilterOption
    on
    Option
    {
        optionId: id
        count
            selected
        urlId
            additionalLabel {
        text
        translationTag {
        translation
        __typename
    }
    __typename
    }
    value
    {
        text
    translationTag
    {
        translation
    __typename
    }
    __typename
    }
    starRating
    {
        value
    symbol
    caption
    {
        translation
    __typename
    }
    showAdditionalInfoIcon
    __typename
    }
    __typename
    }

    fragment
    LandingPageBreadcrumb
    on
    LandingPageBreadcrumb
    {
        destType
    name
    urlParts
    __typename
    }

    fragment
    MatchingUnitConfigurations
    on
    SearchResultProperty
    {
        matchingUnitConfigurations
    {
        commonConfiguration
    {
        name
    unitId
    bedConfigurations
    {
        beds
    {
        count
    type
    __typename
    }
    nbAllBeds
    __typename
    }
    nbAllBeds
    nbBathrooms
    nbBedrooms
    nbKitchens
    nbLivingrooms
    nbUnits
    unitTypeNames
    {
        translation
    __typename
    }
    localizedArea
    {
        localizedArea
    unit
    __typename
    }
    __typename
    }
    unitConfigurations
    {
        name
    unitId
    bedConfigurations
    {
        beds
    {
        count
    type
    __typename
    }
    nbAllBeds
    __typename
    }
    apartmentRooms
    {
        config
    {
        roomId: id
        roomType
            bedTypeId
        bedCount: count
        __typename
    }
    roomName: tag
    {
        tag
    translation
    __typename
    }
    __typename
    }
    nbAllBeds
    nbBathrooms
    nbBedrooms
    nbKitchens
    nbLivingrooms
    nbUnits
    unitTypeNames
    {
        translation
    __typename
    }
    localizedArea
    {
        localizedArea
    unit
    __typename
    }
    unitTypeId
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    PropertyBlocks
    on
    SearchResultProperty
    {
        blocks
    {
        blockId
    {
        roomId
    occupancy
    policyGroupId
    packageId
    mealPlanId
    __typename
    }
    finalPrice
    {
        amount
    currency
    __typename
    }
    originalPrice
    {
        amount
    currency
    __typename
    }
    onlyXLeftMessage
    {
        tag
    variables
    {
        key
    value
    __typename
    }
    translation
    __typename
    }
    freeCancellationUntil
    hasCrib
    blockMatchTags
    {
        childStaysForFree
    __typename
    }
    thirdPartyInventoryContext
    {
        isTpiBlock
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    PriceDisplayInfoIrene
    on
    PriceDisplayInfoIrene
    {
        badges
    {
        name
    {
        translation
    __typename
    }
    tooltip
    {
        translation
    __typename
    }
    style
    identifier
    __typename
    }
    chargesInfo
    {
        translation
    __typename
    }
    displayPrice
    {
        copy
    {
        translation
    __typename
    }
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    __typename
    }
    priceBeforeDiscount
    {
        copy
    {
        translation
    __typename
    }
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    __typename
    }
    rewards
    {
        rewardsList
    {
        termsAndConditions
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    breakdown
    {
        productType
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    __typename
    }
    __typename
    }
    rewardsAggregated
    {
        amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    copy
    {
        translation
    __typename
    }
    __typename
    }
    __typename
    }
    useRoundedAmount
    discounts
    {
        amount
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    name
    {
        translation
    __typename
    }
    description
    {
        translation
    __typename
    }
    itemType
    productId
    __typename
    }
    excludedCharges
    {
        excludeChargesAggregated
    {
        copy
    {
        translation
    __typename
    }
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    __typename
    }
    excludeChargesList
    {
        chargeMode
    chargeInclusion
    chargeType
    amountPerStay
    {
        amount
    amountRounded
    amountUnformatted
    currency
    __typename
    }
    __typename
    }
    __typename
    }
    taxExceptions
    {
        shortDescription
    {
        translation
    __typename
    }
    longDescription
    {
        translation
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    BookerExperienceData
    on
    SearchResultProperty
    {
        bookerExperienceContentUIComponentProps
    {
        ...
    on
    BookerExperienceContentLoyaltyBadgeListProps
    {
        badges
    {
        variant
    key
    title
    popover
    logoSrc
    logoAlt
    __typename
    }
    __typename
    }
    ...
    on
    BookerExperienceContentFinancialBadgeProps
    {
        paymentMethod
    backgroundColor
    hideAccepted
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    SearchMetadata
    on
    SearchMeta
    {
        availabilityInfo
    {
        hasLowAvailability
    unavailabilityPercent
    totalAvailableNotAutoextended
    __typename
    }
    boundingBoxes
    {
        swLat
    swLon
    neLat
    neLon
    type
    __typename
    }
    childrenAges
    dates
    {
        checkin
    checkout
    lengthOfStayInDays
    __typename
    }
    destId
    destType
    maxLengthOfStayInDays
    nbRooms
    nbAdults
    nbChildren
    userHasSelectedFilters
    customerValueStatus
    affiliatePartnerChannelId
    affiliateVerticalType
    affiliateName
    __typename
    }

    fragment
    SearchResultsBreadcrumb
    on
    SearchResultsBreadcrumb
    {
        destId
    destType
    name
    __typename
    }

    fragment
    SorterFields
    on
    SorterOption
    {
        type: name
        captionTranslationTag {
            translation
        __typename
    }
    tooltipTranslationTag
    {
        translation
    __typename
    }
    isSelected: selected
    __typename
    }

    fragment
    OneOfThreeDeal
    on
    OneOfThreeDeal
    {
        id
    uuid
    winnerHotelId
    winnerBlockId
    priceDisplayInfo
    {
        displayPrice
    {
        amountPerStay
    {
        amountRounded
    __typename
    }
    __typename
    }
    __typename
    }
    locationInfo
    {
        name
    inName
    destType
    __typename
    }
    destinationType
    commonFacilities
    {
        id
    name
    __typename
    }
    tpiParams
    {
        wholesalerCode
    rateKey
    rateBlockId
    bookingRoomId
    supplierId
    __typename
    }
    properties
    {
        priceDisplayInfo
    {
        priceBeforeDiscount
    {
        amountPerStay
    {
        amountRounded
    __typename
    }
    __typename
    }
    displayPrice
    {
        amountPerStay
    {
        amountRounded
    __typename
    }
    __typename
    }
    __typename
    }
    basicPropertyData
    {
        id
    name
    pageName
    photos
    {
        main
    {
        highResUrl
    {
        absoluteUrl
    __typename
    }
    __typename
    }
    __typename
    }
    location
    {
        address
    countryCode
    __typename
    }
    reviews
    {
        reviewsCount
    totalScore
    __typename
    }
    __typename
    }
    blocks
    {
        thirdPartyInventoryContext
    {
        rateBlockId
    rateKey
    wholesalerCode
    tpiRoom
    {
        bookingRoomId
    __typename
    }
    supplierId
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    TripTypesData
    on
    TripTypes
    {
        beach
    {
        isBeachUfi
    isEnabledBeachUfi
    isCoastalBeachRegion
    isBeachDestinationWithoutBeach
    __typename
    }
    ski
    {
        isSkiExperience
    isSkiScaleUfi
    __typename
    }
    carouselBeach
    {
        name
    beachId
    photoUrl
    reviewScore
    reviewScoreFormatted
    translatedBeachActivities
    translatedSandType
    __typename
    }
    skiLandmarkData
    {
        resortId
    slopeTotalLengthFormatted
    totalLiftsCount
    __typename
    }
    __typename
    }

    fragment
    ZeroResultsSection
    on
    ZeroResultsSection
    {
        title
    {
        text
    __typename
    }
    primaryAction
    {
        text
    {
        text
    __typename
    }
    action
    {
        name
    __typename
    }
    __typename
    }
    paragraphs
    {
        text
    __typename
    }
    type
    __typename
    }

    fragment
    PreviousSearches
    on
    PreviousSearch
    {
        childrenAges
    __typename
    }

    fragment
    FrontierThemes
    on
    FrontierTheme
    {
        id
    name
    selected
    __typename
    }

    fragment
    MerchRegionIrene
    on
    MerchComponentsResultIrene
    {
        regions
    {
        id
    components
    {
        ...
    on
    PromotionalBannerIrene
    {
        promotionalBannerCampaignId
    contentArea
    {
        title
    {
        ...
    on
    PromotionalBannerSimpleTitleIrene
    {
        value
    __typename
    }
    __typename
    }
    subTitle
    {
        ...
    on
    PromotionalBannerSimpleSubTitleIrene
    {
        value
    __typename
    }
    __typename
    }
    caption
    {
        ...
    on
    PromotionalBannerSimpleCaptionIrene
    {
        value
    __typename
    }
    ...
    on
    PromotionalBannerCountdownCaptionIrene
    {
        campaignEnd
    __typename
    }
    __typename
    }
    buttons
    {
        variant
    cta
    {
        ariaLabel
    text
    targetLanding
    {
        ...
    on
    SearchResultsLandingIrene
    {
        destType
    destId
    checkin
    checkout
    nrAdults
    nrChildren
    childrenAges
    nrRooms
    filters
    {
        name
    value
    __typename
    }
    __typename
    }
    ...
    on
    DirectLinkLandingIrene
    {
        urlPath
    queryParams
    {
        name
    value
    __typename
    }
    __typename
    }
    ...
    on
    LoginLandingIrene
    {
        stub
    __typename
    }
    ...
    on
    DeeplinkLandingIrene
    {
        urlPath
    queryParams
    {
        name
    value
    __typename
    }
    __typename
    }
    ...
    on
    SorterLandingIrene
    {
        sorterName
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }
    designVariant
    {
        ...
    on
    DesktopPromotionalFullBleedImageIrene
    {
        image: image {
        id
        url(width: 814, height: 138)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    DesktopPromotionalImageLeftIrene
    {
        imageOpt: image {
        id
        url(width: 248, height: 248)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    DesktopPromotionalImageRightIrene
    {
        imageOpt: image {
        id
        url(width: 248, height: 248)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalFullBleedImageIrene
    {
        image: image {
        id
        url(width: 358, height: 136)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalImageLeftIrene
    {
        imageOpt: image {
        id
        url(width: 128, height: 128)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalImageRightIrene
    {
        imageOpt: image {
        id
        url(width: 128, height: 128)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalImageTopIrene
    {
        imageOpt: image {
        id
        url(width: 128, height: 128)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalIllustrationLeftIrene
    {
        imageOpt: image {
        id
        url(width: 200, height: 200)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    ...
    on
    MdotPromotionalIllustrationRightIrene
    {
        imageOpt: image {
        id
        url(width: 200, height: 200)
    alt
    overlayGradient
    primaryColorHex
    __typename
    }
    colorScheme
    signature
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }

    fragment
    geniusVipEnrolledProgram
    on
    GeniusVipEnrolledProgram
    {
        metadata
    {
        programType
    __typename
    }
    geniusVipUIs
    {
        searchResultModal
    {
        title
    {
        text
    __typename
    }
    subtitle
    {
        text
    __typename
    }
    modalCategory
    asset
    {
        __typename
        ...on
    Image
    {
        url
    __typename
    }
    }
    cta
    {
        text
    actionString
    actionDismiss
    __typename
    }
    __typename
    }
    __typename
    }
    __typename
    }
    """}
        return payload




    def get_headers(self, offset):
        headers = {
            "authority": "www.booking.com",
            "accept": "*/*",
            "accept-language": "cs-CZ,cs;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5",
            "origin": "https://www.booking.com",
            "referer": f"https://www.booking.com/searchresults.cs.html?label=gog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB&sid=c0b14234663a36fc66ae8b417d55092c&aid=397594&sb=1&sb_lp=1&src=city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcity%2Fcz%2Fprague.cs.html%3Faid%3D397594%26label%3Dgog235jc-1DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB%26sid%3Dc0b14234663a36fc66ae8b417d55092c%26inac%3D0%26%26&ss=Praha&is_ski_area=0&ssne=Praha&ssne_untouched=Praha&city=-553173&checkin_year=2023&checkin_month=11&checkin_monthday=20&checkout_year=2023&checkout_month=11&checkout_monthday=21&flex_window=0&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset={offset}",
            "sec-ch-ua": """"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99""",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "x-booking-context-action-name": "searchresults_irene",
            "x-booking-context-aid": "397594",
            "x-booking-csrf-token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTcwMDE2OTE3NiwiZXhwIjoxNzAwMjU1NTc2fQ.CbeoltdAOTAaGtGZnIyeqVqPmY_S0EEcAiCwOu2I7SmJndEDOTPLE7r7Sc4NncRt1CqDfpsqDy2skNl5Nb8MWg",
            "x-booking-et-serialized-state": "E6sUsaI5c15Vx-LpO8NaeB_dOsT5hsPDaX6WTXMSYty1jECLKAd9yDRqWnGruvWIC",
            "x-booking-pageview-id": "d4b2952c16e7007d",
            "x-booking-site-type-id": "1",
            "x-booking-topic": "capla_browser_b-search-web-searchresults",
            "Content-Type": "application/json"
        }
        return headers





