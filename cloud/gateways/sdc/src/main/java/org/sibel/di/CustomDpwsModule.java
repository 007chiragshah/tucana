package org.sibel.di;

import com.google.inject.AbstractModule;
import com.google.inject.Singleton;
import com.google.inject.assistedinject.FactoryModuleBuilder;
import org.sibel.mdib.overrides.*;
import org.somda.sdc.dpws.DpwsFramework;
import org.somda.sdc.dpws.http.HttpServerRegistry;
import org.somda.sdc.dpws.soap.SoapMarshalling;
import org.somda.sdc.dpws.wsdl.WsdlMarshalling;

public class CustomDpwsModule extends AbstractModule {
    @Override
    protected void configure() {
        bind(CustomJaxbMarshalling.class).asEagerSingleton();
        bind(SoapMarshalling.class).to(CustomJaxbSoapMarshalling.class).asEagerSingleton();
        bind(WsdlMarshalling.class).to(CustomJaxbWsdlMarshalling.class).asEagerSingleton();
        bind(DpwsFramework.class).to(CustomDpwsFrameworkImpl.class).in(Singleton.class);
        bind(HttpServerRegistry.class).to(CustomJettyHttpServerRegistry.class).asEagerSingleton();

        install(new FactoryModuleBuilder().build(CustomJettyHttpServerHandlerFactory.class));
    }
}
