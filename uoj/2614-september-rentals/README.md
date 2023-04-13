<p><a href="https://www.beecrowd.com.br/repository/UOJ_2614_en.html">beecrowd.com.br/repository/UOJ_2614_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2614 </span>
                                    <h1>September Rentals</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>The video store is making its semi-annual report and needs your help. All you have to do is select the name of the clients and the date of rental, from the rentals made in September 2016.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>customers</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>street</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>city</td>
                                  <td>varchar</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>rentals</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>rentals_date</td>
                              <td>date (ISO/YMD)</td>
                            </tr>
                            <tr>
                              <td>id_customers (FK)</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>customers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Giovanna Goncalves Oliveira</td>
                      <td>Rua Mato Grosso</td>
                      <td>Canoas</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Kauã Azevedo Ribeiro</td>
                      <td>Travessa Ibiá</td>
                      <td>Uberlândia</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Rebeca Barbosa Santos</td>
                      <td>Rua Observatório Meteorológico</td>
                      <td>Salvador</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Sarah Carvalho Correia</td>
                      <td>Rua Antônio Carlos da Silva</td>
                      <td>Apucarana</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>João Almeida Lima</td>
                      <td>Rua Rio Taiuva</td>
                      <td>Ponta Grossa</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Diogo Melo Dias</td>
                      <td>Rua Duzentos e Cinqüenta</td>
                      <td>Várzea Grande</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>rentals</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>rentals_date</strong></td>
                  <td><strong>id_customers</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>2016-09-10</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>2016-02-09</td>
                  <td>1</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>2016-02-08</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>2016-02-09</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>2016-02-03</td>
                  <td>6</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>2016-04-04</td>
                  <td>4</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>rentals_date</strong></td>
        </tr>
        <tr>
          <td>Rebeca Barbosa Santos</td>
          <td>2016-09-10</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>